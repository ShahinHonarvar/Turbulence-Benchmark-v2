def palindromes_of_specific_lengths(s):
    sub_string = s[35:89]
    palindromes_of_all_lengths = set()
    for i in range(len(sub_string)):
        for j in range(i + 24, len(sub_string)):
            sub = sub_string[i:j + 1]
            if sub == sub[::-1] and sub.isalpha():
                palindromes_of_all_lengths.add(sub.lower())
    return palindromes_of_all_lengths