def palindromes_of_specific_lengths(s):
    sub_string = s[10:101].lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes