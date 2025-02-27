def palindromes_of_specific_lengths(s):
    palindromes = set()
    sub_str = s[11:97]
    for length in range(45, 53):
        for i in range(len(sub_str) - length + 1):
            sub = sub_str[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes