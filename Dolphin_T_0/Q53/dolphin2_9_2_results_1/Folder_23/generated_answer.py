def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 18, length):
            sub = string[i:j + 1]
            if set(sub) <= set('abcdefghijklmnopqrstuvwxyz'):
                if sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes