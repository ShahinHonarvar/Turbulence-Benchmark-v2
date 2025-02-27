def palindrome_of_length_n(str):
    set_of_palindromes = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            for k in range(j + 1, len(str)):
                substring = str[i:k + 1]
                if palindrome_checker(substring):
                    set_of_palindromes.add(substring)
    if len(set_of_palindromes) == 0:
        return set()
    else:
        return set_of_palindromes

def palindrome_checker(substring):
    str = substring
    str = str.lower()
    p = True
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            p = False
    return p