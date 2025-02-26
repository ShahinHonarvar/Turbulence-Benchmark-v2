def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    sub_s = s[124:284]
    for length in range(115, 135):
        for i in range(len(sub_s) - length + 1):
            substring = sub_s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes