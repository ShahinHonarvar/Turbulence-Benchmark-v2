from sets import Set

def palindromes_between_indices(s):
    result = Set([])
    for i in range(len(s)):
        for j in range(i + 4, min(i + 26, len(s))):
            palindrome = s[i:j + 1][::-1]
            if s[i:j + 1].lower() == palindrome.lower():
                result.add(s[i:j + 1])
    return result