def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    count = 0
    seen = {}
    for s in strings:
        if len(s) < 3:
            continue
        form = canonical_form(s)
        if form in seen:
            count += seen[form]
            if count > 98:
                return False
            seen[form] += 1
        else:
            seen[form] = 1
    return True