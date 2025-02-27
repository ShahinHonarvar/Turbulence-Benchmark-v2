def find_subset_of_length_n(s):
    return len([subset for subset in powerset(s) if len(subset) == 36])

def powerset(s):
    if not s:
        return [set()]
    result = powerset(s[:-1])
    return result + [subset | {s[-1]} for subset in result]