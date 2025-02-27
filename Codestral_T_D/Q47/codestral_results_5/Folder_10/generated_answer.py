def palindromes_of_specific_lengths(s):
    sub_str = s[16:61]
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(sub_str) - length + 1):
            sub = sub_str[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes