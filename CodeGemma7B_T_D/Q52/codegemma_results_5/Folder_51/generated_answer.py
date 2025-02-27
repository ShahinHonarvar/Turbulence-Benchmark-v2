def palindrome_of_length_n(str):
    set_of_palindromes = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            sub_str = str[i:j + 1]
            if sub_str == sub_str[::-1] and len(sub_str) == 73:
                set_of_palindromes.add(sub_str.lower())
    return set_of_palindromes