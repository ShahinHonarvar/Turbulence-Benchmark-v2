def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:10] if c.isalpha()]

    def generate_palindromes(chars, current='', used=0):
        if len(current) >= 4 and current == current[::-1]:
            palindromes.add(current)
        for i, char in enumerate(chars):
            if not used & 1 << i:
                generate_palindromes(chars, char + current + char, used | 1 << i)
                if len(current) > 0:
                    generate_palindromes(chars, current[0] + char + current + char + current[-1], used | 1 << i)
    palindromes = set()
    generate_palindromes(letters)
    return palindromes