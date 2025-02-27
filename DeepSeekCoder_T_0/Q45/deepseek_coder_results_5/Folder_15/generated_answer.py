def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def extract_letters(start, end):
        return ''.join(filter(str.isalpha, s[start:end + 1])).lower()

    def generate_palindromes(letters):
        palindromes = set()
        n = len(letters)
        for i in range(n):
            for j in range(i + 3, n + 1):
                if is_palindrome(letters[i:j]):
                    palindromes.add(letters[i:j])
        return palindromes
    letters = extract_letters(1, 2)
    return generate_palindromes(letters)