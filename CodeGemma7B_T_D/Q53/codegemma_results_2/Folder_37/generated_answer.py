from string import ascii_lowercase

def palindrome_of_length_at_least_n(str):
    return find_palindromes(str, 67, 99999, ascii_lowercase)

def find_palindromes(str, min_len, max_len, letters):
    str = str.lower()
    res = set()
    str_len = len(str)
    for i in range(str_len):
        for j in range(i, str_len):
            if is_palindrome(str[i:j + 1]) and min_len <= j - i + 1 <= max_len and is_letters(str[i:j + 1], letters):
                res.add(str[i:j + 1])
    return res

def is_palindrome(str):
    return str == str[::-1]

def is_letters(str, letters):
    return all((i in letters for i in str))