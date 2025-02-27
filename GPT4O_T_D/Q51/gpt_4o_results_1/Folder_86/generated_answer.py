def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha())))
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_chars(strings[i]) == sorted_chars(strings[j]):
                    count += 1
                    if count > 48:
                        return False
    return True