def palindrome_of_length_at_least_n(string):
    string = string.lower()
    pack_of_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 100, len(string) + 1):
            tmp = string[i:j]
            if tmp == tmp[::-1]:
                pack_of_palindromes.add(tmp)
    return pack_of_palindromes