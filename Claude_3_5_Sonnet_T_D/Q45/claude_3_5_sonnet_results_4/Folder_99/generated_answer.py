def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]

    def generate_palindromes(chars, current='', used=None):
        if used is None:
            used = [False] * len(chars)
        if len(current) >= 3 and current == current[::-1]:
            palindromes.add(current)
        for i in range(len(chars)):
            if not used[i]:
                used[i] = True
                generate_palindromes(chars, current + chars[i], used)
                generate_palindromes(chars, chars[i] + current, used)
                used[i] = False
    palindromes = set()
    generate_palindromes(letters)
    return palindromes