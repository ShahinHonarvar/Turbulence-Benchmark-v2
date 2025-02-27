def palindromes_of_specific_lengths(s):
    sub_s = s[40:90]
    palindromes = set()
    for length in range(23, 39):
        for i in range(0, len(sub_s) - length + 1):
            temp_s = sub_s[i:i + length]
            if temp_s == ''.join(reversed(temp_s)) and temp_s.isalpha():
                palindromes.add(temp_s.lower())
    return palindromes