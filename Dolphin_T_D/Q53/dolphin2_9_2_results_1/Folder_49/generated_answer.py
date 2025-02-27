def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(string) - 72):
        sub_string = string[i:i + 73]
        if set(sub_string).difference(letters) == set():
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes