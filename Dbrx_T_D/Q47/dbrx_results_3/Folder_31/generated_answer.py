def palindromes_of_specific_lengths(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for length in range(37, 61):
        for i in range(11, 84 - length + 1):
            if all((s[i + j].lower() in valid_chars for j in range(length))):
                if s[i:i + length] == s[i:i + length][::-1]:
                    palindromes.add(s[i:i + length])
    return palindromes