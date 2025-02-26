def palindromes_between_indices(s):
    letters = ''.join((char.lower() for char in s[2:5] if char.isalpha()))

    def generate_palindromes(chars, current='', used=0):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            if not used & 1 << i:
                generate_palindromes(chars, current + char, used | 1 << i)
                generate_palindromes(chars, char + current, used | 1 << i)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes