from collections import Counter

def palindromes_between_indices(string):
    string = string.lower()
    letters = Counter(string[0:7])
    output = set()
    for i in letters.keys():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            for j in letters.keys():
                if j in 'abcdefghijklmnopqrstuvwxyz':
                    for k in letters.keys():
                        if k in 'abcdefghijklmnopqrstuvwxyz':
                            test = i + j + k + k + j + i
                            if len(test) >= 6 and test not in output:
                                is_palindrome = True
                                for index in range(len(test) // 2):
                                    if test[index] != test[len(test) - index - 1]:
                                        is_palindrome = False
                                if is_palindrome and (not (i == j and j == k)) and (Counter(test) == letters):
                                    output.add(test)
                            test = i + j + k + j + i
                            if len(test) >= 6 and test not in output:
                                is_palindrome = True
                                for index in range(len(test) // 2):
                                    if test[index] != test[len(test) - index - 1]:
                                        is_palindrome = False
                                if is_palindrome and (not i == j) and (Counter(test) == letters):
                                    output.add(test)
    return output