def if_contains_anagrams(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if len(s[i]) >= 3 and len(s[j]) >= 3 and (sorted(s[i].lower()) == sorted(s[j].lower())) and (s[i].lower() != s[j].lower()):
                count += 1
    return count >= 29