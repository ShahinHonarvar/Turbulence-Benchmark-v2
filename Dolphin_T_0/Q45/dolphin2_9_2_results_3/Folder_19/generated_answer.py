def palindromes_between_indices(string):
    string = string[1:8]
    string = ''.join(sorted(string))
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] != string[j] and string[i:j + 1].lower() == string[i:j + 1].lower()[::-1]:
                palindrome_set.add(string[i:j + 1])
    return palindrome_set