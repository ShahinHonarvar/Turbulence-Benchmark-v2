def palindromes_between_indices(s):
    substring = s[8:10].lower()
    letters = [char for char in substring if char.isalpha()]

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(chars):
        palindromes = set()
        n = len(chars)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    current_chars = [chars[i], chars[j], chars[k]]
                    current_chars.sort()
                    while len(set(current_chars)) >= 3:
                        for arrangement in set(''.join(current_chars)):
                            word = arrangement * 3
                            if is_palindrome(word):
                                palindromes.add(word)
                        break
        return palindromes
    return generate_palindromes(letters)