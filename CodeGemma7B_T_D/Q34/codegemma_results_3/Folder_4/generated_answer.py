def find_original_set(a=set(), b=set(), c=set(), d=set(), e=set(), f=set(), g=set(), h=set(), i=set(), j=set(), k=set(), l=set(), m=set(), n=set(), o=set(), p=set(), q=set(), r=set(), s=set(), t=set(), u=set(), v=set(), w=set(), x=set(), y=set(), z=set(), aa=set(), ab=set(), ac=set(), ad=set(), ae=set(), af=set(), ag=set(), ah=set(), ai=set(), aj=set(), ak=set(), al=set(), am=set(), an=set(), ao=set(), ap=set(), aq=set(), ar=set(), as_=set(), at=set(), au=set(), av=set(), aw=set(), ax=set(), ay=set(), az=set()):
    """
    Finds the smallest set that contains all of the input sets.

    Args:
        *a-z: Sets of integers.

    Returns:
        A set containing the smallest set that contains all of the input sets.
    """
    sets = sorted(locals().values(), key=len)
    original_set = sets[0]
    for set in sets[1:]:
        original_set |= set
    return original_set