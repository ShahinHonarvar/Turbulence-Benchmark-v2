def palindromes_of_specific_lengths(s):
    sub_string = s[26:85]
    palindromes = set()
    for length in range(30, 47):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length].lower()
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes