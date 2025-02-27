def palindromes_between_indices(s):
    English_letters = 'abcdefghijklmnopqrstuvwxyz'.lower()
    palindromes = set()
    sub_string = s[4:10]
    for p in range(6, len(sub_string) + 1):
        for i in range(len(sub_string)):
            for j in range(i + p, len(sub_string) + 1):
                sub = sub_string[i:j]
                if sub == sub[::-1]:
                    palindromes.add(sub.lower())
    return palindromes