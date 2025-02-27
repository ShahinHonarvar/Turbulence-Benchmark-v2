def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    if len(letters) < 7:
        return palindromes

    def generate_palindromes(current, remaining, length):
        if length == 0:
            if current == current[::-1]:
                palindromes.add(current)
        else:
            for i in range(len(remaining)):
                generate_palindromes(current + remaining[i], remaining[:i] + remaining[i + 1:], length - 1)
    generate_palindromes('', letters, 7)
    return palindromes