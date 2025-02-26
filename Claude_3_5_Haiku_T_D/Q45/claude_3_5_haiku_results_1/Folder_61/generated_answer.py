def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [char.lower() for char in s[:8] if char.isalpha()]

    def generate_palindromes(available_letters):
        palindromes = set()

        def backtrack(current_palindrome, remaining_letters):
            if len(current_palindrome) >= 7 and is_palindrome(current_palindrome):
                palindromes.add(current_palindrome)
            if len(current_palindrome) == 2 * (len(current_palindrome) // 2):
                mid = len(current_palindrome) // 2
                left = current_palindrome[:mid]
                right = current_palindrome[mid:]
                if is_palindrome(left + right):
                    palindromes.add(current_palindrome)
            for i in range(len(remaining_letters)):
                letter = remaining_letters[i]
                new_remaining = remaining_letters[:i] + remaining_letters[i + 1:]
                backtrack(current_palindrome + letter, new_remaining)
        backtrack('', available_letters)
        return {p for p in palindromes if len(p) >= 7}
    return generate_palindromes(letters)