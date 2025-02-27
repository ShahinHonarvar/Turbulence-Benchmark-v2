def palindromes_of_specific_lengths(s):
    subs = s[0:5]
    subs = subs.lower()
    palindrome_set = set()
    for i in range(len(subs)):
        if subs[i:i + 3].isalpha() and subs[i:i + 3] == subs[i:i + 3][::-1]:
            palindrome_set.add(subs[i:i + 3])
        if subs[i:i + 4].isalpha() and subs[i:i + 4] == subs[i:i + 4][::-1]:
            palindrome_set.add(subs[i:i + 4])
    return palindrome_set