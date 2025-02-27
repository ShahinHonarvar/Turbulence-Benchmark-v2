def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 42, len(s) + 1):
            subs = s[i:j].lower()
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result