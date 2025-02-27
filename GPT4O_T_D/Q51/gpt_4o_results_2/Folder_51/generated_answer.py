def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    strings = [s for s in strings if len(s) >= 3]
    seen = {}
    pair_count = 0
    for s in strings:
        can_form = canonical_form(s)
        if can_form in seen:
            pair_count += seen[can_form]
            if pair_count > 116:
                return False
            seen[can_form] += 1
        else:
            seen[can_form] = 1
    return True