def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:7] if char.isalpha()]
    if len(letters) < 4:
        return set()

    def generate_palindromes(letters):

        def backtrack(current_palindrome, remaining_letters):
            if len(current_palindrome) >= 4 and current_palindrome == current_palindrome[::-1]:
                result.add(current_palindrome)
            for i in range(len(remaining_letters)):
                backtrack(current_palindrome + remaining_letters[i], remaining_letters[:i] + remaining_letters[i + 1:])
        result = set()
        backtrack('', letters)
        return result
    return generate_palindromes(letters)