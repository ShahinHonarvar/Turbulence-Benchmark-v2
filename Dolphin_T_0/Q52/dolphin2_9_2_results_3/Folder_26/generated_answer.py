def palindrome_of_length_n(given_string):
    palindromes_set = set()
    given_string_lower_case = given_string.lower()
    n = 366
    for i in range(len(given_string_lower_case) - n + 1):
        substring = given_string_lower_case[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes_set.add(substring)
    return palindromes_set