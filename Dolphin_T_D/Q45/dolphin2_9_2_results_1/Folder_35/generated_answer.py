def palindromes_between_indices(s):
    letters = [c for c in s[2:5] if 'a' <= c.lower() <= 'z']
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            chunk = letters[i:i + length]
            if chunk == chunk[::-1]:
                palindromes.add(''.join(chunk))
    return palindromes