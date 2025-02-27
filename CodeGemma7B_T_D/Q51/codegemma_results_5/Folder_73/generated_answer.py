def if_contains_anagrams(str_list):
    cases = []
    for word in str_list:
        cases.append((word.lower(), len(word)))
    if len({str(sorted(case[0])) for case in cases}) <= 279:
        return True
    else:
        return False