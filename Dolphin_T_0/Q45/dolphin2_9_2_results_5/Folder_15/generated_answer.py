def palindromes_between_indices(string):
    string = string[1:3]
    string = ''.join(filter(str.isalpha, string)).lower()
    n = len(string)
    if n < 3:
        return set()
    palindromes = set([])
    for i in range(n):
        for j in range(i + 2, n):
            if string[i] == string[j]:
                sub_string = string[i:j + 1]
                if sub_string == sub_string[::-1]:
                    palindromes.add(sub_string)
    return palindromes