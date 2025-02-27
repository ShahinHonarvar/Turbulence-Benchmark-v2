def palindromes_of_specific_lengths(s):
    s = s[30:91]
    lengths = [50, 51, 52, 53]
    set_palindromes = set()
    for length in lengths:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1].lower():
                set_palindromes.add(substring)
    return set_palindromes