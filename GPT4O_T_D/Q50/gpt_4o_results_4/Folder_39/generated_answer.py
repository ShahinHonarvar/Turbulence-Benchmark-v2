def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    memo = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        form = canonical_form(string)
        if form in memo:
            count += memo[form]
            if count >= 54:
                return True
            memo[form] += 1
        else:
            memo[form] = 1
    return False