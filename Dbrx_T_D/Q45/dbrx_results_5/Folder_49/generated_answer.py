from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    english_letters = defaultdict(list)
    for i in range(5, 8):
        if s[i].isalpha():
            english_letters[s[i]].append(i)
    palindromes = set()
    for indices in english_letters.values():
        if len(indices) >= 3:
            for i in range(len(indices) - 2):
                for j in range(i + 2, len(indices)):
                    palindrome = s[indices[i]:indices[i] + 1] + s[indices[i] + 1:indices[j]][::-1] + s[indices[i] + 1:indices[j]][1:] + s[indices[i]:indices[i] + 1][::-1]
                    palindromes.add(palindrome)
    return palindromes