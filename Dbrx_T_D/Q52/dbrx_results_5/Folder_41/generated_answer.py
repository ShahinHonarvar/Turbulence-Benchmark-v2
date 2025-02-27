def palindrome_of_length_n(string):
    n = 60
    pallist = set()
    string = ''.join((e for e in string if e.isalpha())).lower()
    if len(string) < n:
        return pallist
    for i in range(len(string) - n + 1):
        sub = string[i:i + n]
        if sub == sub[::-1]:
            pallist.add(sub)
    return pallist