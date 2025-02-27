def palindrome_of_length_n(str):
    str_lower = str.lower()
    Palindromes = set()
    for i in range(len(str_lower)):
        for j in range(i + 475, len(str_lower) + 1):
            if str_lower[i:j] == str_lower[i:j][::-1]:
                Palindromes.add(str[i:j])
    if not Palindromes:
        Palindromes = set()
    return Palindromes