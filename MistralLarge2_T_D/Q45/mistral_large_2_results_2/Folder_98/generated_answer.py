def palindromes_between_indices(s):
    letters = [ch for ch in s[3:6] if ch.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, length):
        if length == 0:
            if is_palindrome(current) and len(current) >= 4:
                palindromes.add(current)
            return
        for letter in letters:
            generate_palindromes(current + letter, length - 1)
    for length in range(4, len(letters) + 1):
        generate_palindromes('', length)
    return palindromes