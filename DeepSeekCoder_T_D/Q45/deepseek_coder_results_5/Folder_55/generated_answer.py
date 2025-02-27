def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]

    def get_letters_in_range(start, end):
        return ''.join(filter(str.isalpha, s[start:end + 1])).lower()

    def generate_palindromes(letters):
        palindromes = set()
        for i in range(len(letters)):
            for j in range(i + 3, len(letters) + 1):
                if is_palindrome(letters[i:j]):
                    palindromes.add(letters[i:j])
        return palindromes
    letters = get_letters_in_range(0, 2)
    return generate_palindromes(letters)