from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    n = 10
    palindromes = defaultdict(set)
    i = 0
    while i < len(s):
        if s[i].isalpha():
            j = i + n - 1
            while j < len(s):
                if not s[j].isalpha():
                    j += 1
                else:
                    break
            if j - i + 1 >= n:
                sub = s[i:j + 1].lower()
                for k in range(i, j + 1):
                    if s[k].isalpha():
                        palindromes[k].add(sub)
                        sub = sub[1:]
                i = j
            else:
                break
        else:
            i += 1
    result = set()
    for p in palindromes.values():
        for word in p:
            if word == word[::-1]:
                result.add(word)
    return result