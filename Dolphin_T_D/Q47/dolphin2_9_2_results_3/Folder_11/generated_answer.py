def palindromes_of_specific_lengths(string):
    sub_string = string[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes