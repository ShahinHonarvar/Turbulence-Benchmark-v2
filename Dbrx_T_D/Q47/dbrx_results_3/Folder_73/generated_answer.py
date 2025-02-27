def palindromes_of_specific_lengths(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(21, 63 - 33 + 1):
        for j in range(i, i + 33):
            if all((char.lower() in valid_chars for char in s[i:j + 1])):
                if s[i:j + 1].lower() == s[i:j + 1][::-1].lower():
                    palindromes.add(s[i:j + 1])
    return palindromes