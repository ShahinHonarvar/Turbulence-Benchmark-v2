def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    palindromes = set()

    def generate_palindromes(available_letters):
        for length in range(4, len(available_letters) * 2 + 1, 2):

            def backtrack(current_palindrome, remaining_letters):
                if len(current_palindrome) == length:
                    palindromes.add(current_palindrome)
                    return
                for i in range(len(remaining_letters)):
                    letter = remaining_letters[i]
                    new_remaining = remaining_letters[:i] + remaining_letters[i + 1:]
                    backtrack(letter + current_palindrome + letter, new_remaining)
            backtrack('', available_letters)
    generate_palindromes(letters)
    return palindromes