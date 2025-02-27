from collections import defaultdict

def palindrome_of_length_at_least_n(s):

    def isPalindrome(word):
        return word == word[::-1]
    letters = defaultdict(list)
    for i, char in enumerate(s.lower()):
        letters[char].append(i)
    res = set()
    for char, indexes in letters.items():
        for i in range(len(indexes)):
            for j in range(i + 1, len(indexes)):
                for k in range(j + 1, len(indexes)):
                    for l in range(k + 1, len(indexes)):
                        for m in range(l + 1, len(indexes)):
                            for n in range(m + 1, len(indexes)):
                                for o in range(n + 1, len(indexes)):
                                    for p in range(o + 1, len(indexes)):
                                        palindrome = [char]
                                        for idx in range(i, o + 1):
                                            palindrome.append(s[indexes[idx]])
                                        for idx in range(p, l - 1, -1):
                                            palindrome.append(s[indexes[idx]])
                                        palindrome.append(char)
                                        if isPalindrome(palindrome) and len(palindrome) >= 87:
                                            res.add(''.join(palindrome).upper())
    return res