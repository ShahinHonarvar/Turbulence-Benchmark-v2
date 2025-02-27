import re
  from collections import Counter

def palindromes_between_indices(string):
    string = string[2:10].lower()
    string = ''.join(re.findall('[a-z]', string))
    letters = Counter(string)
    middles = []
    palindromes = set()
    for letter in letters:
        if letters[letter] >= 2:
            middles.append(letter * (letters[letter] // 2 * 2))
    if len(middles) == 0:
        return set()
    for i in range(len(middles)):
        for j in range(i, len(middles)):
            for k in range(len(middles)):
                for l in range(len(middles[k])):
                    for m in range(l + 1, len(middles[k]) + 1):
                        palindrome = middles[i] + middles[j] + middles[k][l:m]
                        if len(palindrome) >= 7:
                            palindromes.add(palindrome)
                        palindrome = middles[k][l:m] + middles[i] + middles[j]
                        if len(palindrome) >= 7:
                            palindromes.add(palindrome)
    return palindromes