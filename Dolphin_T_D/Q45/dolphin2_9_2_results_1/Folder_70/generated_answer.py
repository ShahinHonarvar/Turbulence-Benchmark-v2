def palindromes_between_indices(s):
    s = s[1:7]
    letters = set([ch.lower() for ch in s if ch.isalpha()])
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    possible = English_letters.intersection(letters)
    if len(possible) < 4:
        return set()
    palindromes = set()
    length = len(possible)
    for i in range(length):
        for j in range(length):
            palindrome = possible.copy()
            palindrome.remove(possible.pop() if i else possible.pop(0))
            palindrome.remove(possible.pop() if j else possible.pop(0))
            palindrome = ''.join(palindrome)
            if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes