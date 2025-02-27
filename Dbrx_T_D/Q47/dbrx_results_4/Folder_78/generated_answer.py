from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    s = s[14:73].lower()
    return {palindrome[i:j] for i in range(55) for j in range(i + 19, 56) if (palindrome := s[i:j]) == palindrome[::-1]}