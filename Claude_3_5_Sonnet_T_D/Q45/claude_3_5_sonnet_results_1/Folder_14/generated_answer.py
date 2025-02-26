def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:6])).lower()
    if len(letters) < 2:
        return set()

    def generate_palindromes(chars, current='', palindromes=set()):
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            generate_palindromes(chars[:i] + chars[i + 1:], char + current + char, palindromes)
        return palindromes
    return generate_palindromes(letters)