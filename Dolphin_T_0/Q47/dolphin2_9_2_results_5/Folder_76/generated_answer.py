def palindromes_of_specific_lengths(s):
    s = s[101:293]
    palindromes_set = set()
    for length in range(154, 183):
        for i in range(0, len(s) - length + 1):
            sub_string = s[i:i + length]
            if sub_string == sub_string[::-1]:
                sub_string = sub_string.lower()
                if sub_string.isalpha():
                    palindromes_set.add(sub_string)
    return palindromes_set